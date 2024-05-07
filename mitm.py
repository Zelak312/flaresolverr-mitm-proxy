import os
import json
import base64
import urllib.parse
from mitmproxy import ctx

special_prefix_token = os.environ.get("SPECIAL_PREFIX_TOKEN", "$$")
header_split_token = os.environ.get("HEADER_SPLIT_TOKEN", ":")
header_token = f"{special_prefix_token}headers[]"
post_token = f"{special_prefix_token}post"

class FlaresolverrProxy:
    def handle_headers(self, flow):
        if header_token in flow.request.query:
            headers = flow.request.query.get_all(header_token)
            for header in headers:
                if not header_split_token in header:
                    continue

                [key, value] = header.split(header_split_token, 1)
                flow.request.headers[key] = value
            flow.request.query.pop(header_token, None)

    def handle_post_json(self, flow):
        # Parse the post data
        try:
            form_data = urllib.parse.parse_qs(flow.request.get_text())
        except Exception as e:
            ctx.log.error(f"Failed to parse form data: {e}")
            return

        if post_token in form_data:
            # Check if the form data contains the post token
            if not post_token in form_data:
                return

            # Try to decode the post data
            try:
                # Ensure the string is correctly padded
                missing_padding = len(form_data[post_token][0]) % 4
                if missing_padding:
                    form_data[post_token][0] += '=' * (4 - missing_padding)

                decoded_string = base64.b64decode(
                    form_data[post_token][0]).decode("utf-8")
            except Exception as e:
                return

            # Try to parse the post data as JSON
            try:
                post_data = json.loads(decoded_string)
            except Exception as e:
                return

            # Change header to JSON
            flow.request.headers["Content-Type"] = "application/json"
            # Set the JSON data as the request body
            flow.request.set_text(json.dumps(post_data))

    def request(self, flow):
        # Handle headers
        self.handle_headers(flow)
        # Handle post json if needed
        if flow.request.method == "POST":
            self.handle_post_json(flow)

addons = [
    FlaresolverrProxy()
]
