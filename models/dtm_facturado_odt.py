from odoo import models,api,fields

class ODTFacturado (models.Model):
    _name = "dtm.facturado.odt"
    _description ="Modulo para llevar el historial de las ordenes de trabajo con factura"
    _order = "ot_number desc"


    status = fields.Char(string="Factura/s",readonly=True)
    ot_number = fields.Integer(string="NÚMERO",readonly=True)
    tipe_order = fields.Char(string="TIPO",readonly=True)
    name_client = fields.Char(string="CLIENTE",readonly=True)
    product_name = fields.Char(string="NOMBRE DEL PRODUCTO",readonly=True)
    date_in = fields.Date(string="FECHA DE ENTRADA", readonly=True)
    po_number = fields.Char(string="PO",readonly=True)
    date_rel = fields.Date(string="FECHA DE ENTREGA",readonly=True)
    version_ot = fields.Integer(string="VERSIÓN OT",readonly=True)
    color = fields.Char(string="COLOR",default="N/A",readonly=True)
    cuantity = fields.Integer(string="CANTIDAD",readonly=True)
    materials_ids = fields.Many2many("dtm.materials.line",readonly=True)
    firma = fields.Char(string="Firma", readonly = True)
    firma_compras = fields.Char()
    firma_diseno = fields.Char()
    firma_almacen = fields.Char()
    firma_ventas = fields.Char()
    firma_calidad = fields.Char()

    planos = fields.Boolean(string="Planos",default=False, readonly=True)
    nesteos = fields.Boolean(string="Nesteos",default=False, readonly=True)

    rechazo_id = fields.Many2many("dtm.odt.rechazo")
    anexos_id = fields.Many2many("dtm.proceso.anexos",readonly=True)
    cortadora_id = fields.Many2many("dtm.proceso.cortadora",readonly=True)
    primera_pieza_id = fields.Many2many("dtm.proceso.primer",readonly=True)
    tubos_id = fields.Many2many("dtm.proceso.tubos",readonly=True)

    #---------------------Resumen de descripción------------

    description = fields.Text(string="DESCRIPCIÓN",readonly=True)

    #------------------------Notas---------------------------

    notes = fields.Text(string="notes")

    def action_imprimir_formato(self): # Imprime según el formato que se esté llenando
        return self.env.ref("dtm_odt.formato_orden_de_trabajo").report_action(self)

    def action_imprimir_materiales(self): # Imprime según el formato que se esté llenando
        return self.env.ref("dtm_odt.formato_lista_materiales").report_action(self)
