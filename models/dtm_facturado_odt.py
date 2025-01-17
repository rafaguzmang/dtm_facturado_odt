from odoo import models,api,fields

class ODTFacturado (models.Model):
    _name = "dtm.facturado.odt"
    _description ="Modulo para llevar el historial de las ordenes de trabajo con factura"
    _order = "ot_number desc"
    _rec_name = "ot_number"



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
    # materials_ids = fields.Many2many("dtm.materials.line",readonly=True)
    materieales_id = fields.One2many("dtm.facturado.materiales","model_id",readonly=True)
    firma = fields.Char(string="Firma", readonly = True)
    firma_compras = fields.Char()
    firma_diseno = fields.Char()
    firma_almacen = fields.Char()
    firma_ventas = fields.Char()
    firma_calidad = fields.Char()

    planos = fields.Boolean(string="Planos",default=False, readonly=True)
    nesteos = fields.Boolean(string="Nesteos",default=False, readonly=True)

    rechazo_id = fields.Many2many("dtm.proceso.rechazo")
    anexos_id = fields.Many2many("dtm.proceso.anexos",readonly=True)
    cortadora_id = fields.Many2many("dtm.proceso.cortadora",readonly=True)
    primera_pieza_id = fields.Many2many("dtm.proceso.primer",readonly=True)
    tubos_id = fields.Many2many("dtm.proceso.tubos",readonly=True)
    calidad_liberacion = fields.Many2many("dtm.proceso.liberacion",readonly=True)

    #---------------------Resumen de descripción------------

    description = fields.Text(string="DESCRIPCIÓN",readonly=True)

    #------------------------Notas---------------------------

    notes = fields.Text(string="notes")

    def action_imprimir_formato(self): # Imprime según el formato que se esté llenando
        return self.env.ref("dtm_odt.formato_orden_de_trabajo").report_action(self)

    def action_imprimir_materiales(self): # Imprime según el formato que se esté llenando
        return self.env.ref("dtm_odt.formato_lista_materiales").report_action(self)

class Materiales(models.Model):
    _name = "dtm.facturado.materiales"
    _description = "Se guarda el registro de los materiales utilizados"
    npi_id = fields.Many2one('dtm.facturado.npi')
    model_id = fields.Many2one("dtm.facturado.odt")
    material = fields.Char(string = "Material")
    cantidad = fields.Integer()

class NPIterminado (models.Model):
    _name = "dtm.facturado.npi"
    _description ="Modulo para llevar el historial de las ordenes de trabajo con factura"
    _order = "ot_number desc"
    _rec_name = "ot_number"

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
    materieales_id = fields.One2many("dtm.facturado.materiales","npi_id",readonly=True)
    firma = fields.Char(string="Firma", readonly = True)
    firma_compras = fields.Char()
    firma_diseno = fields.Char()
    firma_almacen = fields.Char()
    firma_ventas = fields.Char()
    firma_calidad = fields.Char()

    planos = fields.Boolean(string="Planos",default=False, readonly=True)
    nesteos = fields.Boolean(string="Nesteos",default=False, readonly=True)

    rechazo_id = fields.Many2many("dtm.proceso.rechazo")
    anexos_id = fields.Many2many("dtm.proceso.anexos",readonly=True)
    cortadora_id = fields.Many2many("dtm.proceso.cortadora",readonly=True)
    primera_pieza_id = fields.Many2many("dtm.proceso.primer",readonly=True)
    tubos_id = fields.Many2many("dtm.proceso.tubos",readonly=True)
    calidad_liberacion = fields.Many2many("dtm.proceso.liberacion",readonly=True)



    #---------------------Resumen de descripción------------

    description = fields.Text(string="DESCRIPCIÓN",readonly=True)

    #------------------------Notas---------------------------

    notes = fields.Text(string="notes")

    def action_imprimir_formato(self): # Imprime según el formato que se esté llenando
        return self.env.ref("dtm_odt.formato_orden_de_trabajo").report_action(self)

    def action_imprimir_materiales(self): # Imprime según el formato que se esté llenando
        return self.env.ref("dtm_odt.formato_lista_materiales").report_action(self)

    # def get_view(self, view_id=None, view_type='form', **options):
    #     res = super(ODTFacturado,self).get_view(view_id, view_type,**options)
    #
    #     get_self = self.env['dtm.facturado.odt'].search([])
    #     for result in get_self:
    #         for record in result:
    #             lines = []
    #             for item in record.materials_ids:
    #                 nombre = ""
    #                 medida =""
    #                 cantidad = 0
    #                 if item.nombre:
    #                     nombre = item.nombre
    #                 if item.medida:
    #                     medida = item.medida
    #                 if item.materials_cuantity:
    #                     cantidad = item.materials_cuantity
    #                 dato = f"{nombre} {medida}"
    #                 vals = {
    #                     "material":dato,
    #                     "cantidad":cantidad
    #                 }
    #                 get_item = self.env['dtm.facturado.materiales'].search([("model_id","=",self._origin.id),("material","=",dato),("cantidad","=",cantidad)])
    #                 if get_item:
    #                     get_item.write(vals)
    #                     lines.append(get_item.id)
    #                 else:
    #                     get_item.create(vals)
    #                     get_item = self.env['dtm.facturado.materiales'].search([("model_id","=",self._origin.id),("material","=",dato),("cantidad","=",cantidad)])
    #                     lines.append(get_item.id)
    #             record.write({'materieales_id': [(5, 0, {})]})
    #             record.write({'materieales_id': [(6, 0, lines)]})
    #             self.env['dtm.materials.line'].browse(lines)
    #
    #     return res




