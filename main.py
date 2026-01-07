from src import GoogleSheet, Monetarias


def main():
    monetarias = Monetarias()

    sheet_map = {
        'tipo_cambio_minorista': {
            'id': '184L6JQn2TZIy_5rzZbIhKA78p03BlBhVZLGXIW8Mi9o',
            'from_date': '2019-12-31'
            },
        'tasa_depositos_30': {
            'id': '1WCA_-_Xaq1bZcStdyVyxNUrdsdqkDLQ6hjODyH3FcIQ',
            'from_date': '2019-12-31'
            },
        'ipc_interanual': {
            'id': '1Cjbw6OfPJ9CkB8SmY73ZYlvc2afeMNltlBARL7TK95I',
            'from_date': '2019-12-31'
            },
        'ipc_mensual': {
            'id': '1bFUt87NufZOi4QbYAtO0Yz-iNKFMSfEGVEW0iMkiuOg',
            'from_date': '2019-12-31'
            }
    }
    
    for sheet_name, _map in sheet_map.items():
        sheet_id = _map.get('id', None)
        from_date = _map.get('from_date', None)

        bcra_data = monetarias.get_data(sheet_name, from_date)

        google_sheet = GoogleSheet(spreadsheet_id=sheet_id)
        google_sheet.upload_to_sheets(
            fieldnames=['fecha', 'valor'],
            data_dicts=bcra_data['results'][0]['detalle']
        )


if __name__ == "__main__":
   main()
