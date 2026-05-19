{
    "name":"Facturado",
    'version': '1.0',
    'author': "Rafael Guzmán",
    "description": "Modulo para llevar el historial de las OTs",
    "depends":["dtm_procesos"],
    "data":[
        # Security
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        # Views
        'views/dtm_facturado_odt_view.xml',
        'views/dtm_facturado_npi_view.xml',
        'views/dtm_facturado_retrabajo_view.xml',
         #Reports
        'reports/orden_de_trabajo.xml',
        'reports/lista_materiales.xml',
    ],
    'license': 'LGPL-3',
}

