from src import Monetarias, project_paths
from google_sheet_util import GoogleSheet


def main():
    monetarias = Monetarias()

    sheet_map = {
        'ipc_mensual': {
            'id': '1bFUt87NufZOi4QbYAtO0Yz-iNKFMSfEGVEW0iMkiuOg',
            'from_date': '2019-12-31',
            'fieldnames': ['fecha', 'valor'],
            'column_formats': {
                'fecha': 'date',
                'valor': 'currency'
            }
        }
    }

    for sheet_name, _map in sheet_map.items():
        sheet_id = _map.get('id', None)
        from_date = _map.get('from_date', None)
        fieldnames = _map.get('fieldnames', [])
        column_formats = _map.get('column_formats', {})

        bcra_data = monetarias.get_data(sheet_name, from_date)

        google_sheet = GoogleSheet(
            credentials=project_paths.get_credentials(),
            token=project_paths.get_token(),
            spreadsheet_id=sheet_id
        )
        google_sheet.upload_to_sheets(
            fieldnames=fieldnames,
            column_formats=column_formats,
            data_dicts=bcra_data
        )


if __name__ == "__main__":
   main()
