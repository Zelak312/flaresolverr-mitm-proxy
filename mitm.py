# addon_example.py
import json
import urllib.parse
from mitmproxy import ctx


def set_nested_item(dataDict, mapList, value):
    for k in mapList[:-1]:
        dataDict = dataDict.setdefault(k, {})
    dataDict[mapList[-1]] = value


class FlaresolverrProxy:
    def request(self, flow):
        content_type = flow.request.headers.get("Content-Type", "")

        headers = {}
        if flow.request.method == "GET":
            ctx.log.debug("Checking request for GET")
            form_data = flow.request.query
            if "$headers$[]" in form_data:
                ctx.log.debug("Found $headers$[] in query")
                # Remove the $headers$[] key
                headers = form_data.pop("$headers$[]")
                # Remove the $headers$[] key from the query
                flow.request.query.pop("$headers$[]")
        elif "application/x-www-form-urlencoded" in content_type and flow.request.method == "POST":
            request_txt = flow.request.get_text().strip()
            if request_txt == "":
                return

            ctx.log.debug("Checking request for POST")
            try:
                form_data = urllib.parse.parse_qs(request_txt)
            except Exception as e:
                ctx.log.error(f"Failed to parse form data: {e}")
                return

            if "$headers$[]" in form_data:
                ctx.log.debug("Found $headers$[] in form data")
                # Remove the $headers$ key
                headers = form_data.pop("$headers$[]")

            if "$post$" in form_data and form_data["$post$"][0] == "true":
                # Remove the $post$ key
                form_data.pop("$post$")

                # Convert the form data to a nested dict
                nested_data = {}
                for key, value in form_data.items():
                    if key.endswith("[]"):
                        key = key[:-2]
                        set_nested_item(nested_data, key.split('.'), value)
                    else:
                        set_nested_item(nested_data, key.split('.'), value[0])

                # Set the content type to JSON and update the request body
                flow.request.headers["Content-Type"] = "application/json"
                flow.request.set_text(json.dumps(nested_data))

        if len(headers) > 0:
            for header in headers:
                if not ":" in header:
                    continue

                [key, value] = header.split(":")
                ctx.log.debug(f"Setting header {key} to {value}")
                print(f"Setting header {key} to {value}")
                flow.request.headers[key] = value


addons = [
    FlaresolverrProxy()
]
