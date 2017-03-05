#-*-encoding:utf-8-*-
from openerp import models, fields

class propietari(models.Model):
	_name='taller.propietari'
	nom=fields.Char('Nom', size=150, required=True)
	telf=fields.Char('Telf', size=9)
	adreca=fields.Char('Adreça', size=50)
	_rec_name='nom'

class cotxe(models.Model):
	_name='taller.cotxe'
	tipus= fields.Selection([('cotxe', 'Cotxe'),('moto', 'Moto'),('camio', 'Camió'),('bici', 'Bicicleta')])
	marca=fields.Char('Marca', size=50)
	model=fields.Char('Model', size=50)
	color=fields.Char('Color', size=10)
	portes=fields.Integer('Portes')
	matricula=fields.Char('Matricula', size=7, required=True)
	numbastidor=fields.Char('Num Bastidor', size=20)
	combustible=fields.Selection([('diesel','Diesel'), ('gasolina', 'Gasolina')])
	comentaris=fields.Text('Comentaris')
	propietari=fields.Many2one('taller.propietari', required=True)
	data_entrada=fields.Date('Data entrada')
	_rec_name='model'
	reparat=fields.Boolean('Reparat')
	datasortida=fields.Date('Data de sortida')

class mecanics(models.Model):
	_name='taller.mecanic'
	dni=fields.Char('DNI', size=9, required=True)
	nom=fields.Char('Nom', size=50)
	cognom=fields.Char('Cognom', size=50)
	reparacions=fields.Many2many('taller.cotxe','reparacio', 'dni', 'matricula')
	
