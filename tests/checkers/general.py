import json
import jsonschema

from tests.configuration import base_path


class CheckerGeneral:
    @staticmethod
    def validate_json(response_dict: dict, path_to_schema: str):
        with open(base_path + path_to_schema) as f:
            schema = json.load(f)

        jsonschema.validate(response_dict, schema)
        return True

    def validate_items(self, items: list[dict], path_to_schema: str):
        for item in items:
            self.validate_json(item, path_to_schema)

        return True
