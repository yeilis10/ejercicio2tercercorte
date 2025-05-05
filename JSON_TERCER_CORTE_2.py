import json

# JSON actualizado con más productos
json_data = '''
{
  "nombre_tienda": "Luz del Día",
  "ubicacion": "Medellín, Colombia",
  "moneda": "COP",
  "inventario": {
    "en_tienda": [
      {
        "categoria": "Vestidos",
        "producto": {
          "nombre": "Vestido Pegado abierto en la pierna",
          "cantidad": 15,
          "precio": 70000,
          "descuento": 10,
          "en_tendencia": true,
          "tallas": ["talla UNICA"]
        }
      },
      {
        "categoria": "Pantalones",
        "producto": {
          "nombre": "Pantalón cargo ",
          "cantidad": 10,
          "precio": 100000,
          "descuento": 0,
          "en_tendencia": true,
          "tallas": ["M", "L","XS"]
        }
      },
      {
        "categoria": "Chaquetas",
        "producto": {
          "nombre": "Chaqueta de cuero",
          "cantidad": 4,
          "precio": 150000,
          "descuento": 5,
          "en_tendencia": false,
          "tallas": ["S", "M", "L", "XL"]
        }
      },
      {
        "categoria": "Chores",
        "producto": {
          "nombre": "Chores ",
          "cantidad": 10,
          "precio": 89900,
          "descuento": 10,
          "en_tendencia": true,
          "tallas": ["S", "M", "L", "XS"]
        }
      },
      {
        "categoria": "Jeans",
        "producto": {
          "nombre": "Jeans",
          "cantidad": 12,
          "precio": 139000,
          "descuento": 5,
          "en_tendencia": true,
          "tallas": ["todas las tallas"]
        }
      },
      {
        "categoria": "Conjuntos",
        "producto": {
          "nombre": "Conjunto de mujer de 3 piezas de color azul,marron.rojo y verde",
          "cantidad": 10,
          "precio": 90000,
          "descuento": 20,
          "en_tendencia": false,
          "tallas": ["talla unica"]
        }
      },
      {
        "categoria": "Pijamas",
        "producto": {
          "nombre": "Pijama de algodón rosa,roja y azul",
          "cantidad": 8,
          "precio": 79900,
          "descuento": 10,
          "en_tendencia": true,
          "tallas": ["todas las tallas"]
        }
      },
      {
        "categoria": "Faldas",
        "producto": {
          "nombre": "Falda cargo",
          "cantidad": 10,
          "precio": 90000,
          "descuento": 5,
          "en_tendencia": true,
          "tallas": ["todas las tallas"]
        }
      },
      {
        "categoria": "Blusas cortas",
        "producto": {
          "nombre": "Blusa corta de lino blanca y negra",
          "cantidad": 12,
          "precio": 50000,
          "descuento": 0,
          "en_tendencia": true,
          "tallas": ["todas las tallas"]
        }
      },
      {
        "categoria": "Blusas largas",
        "producto": {
          "nombre": "Blusas ",
          "cantidad": 6,
          "precio": 50000,
          "descuento": 5,
          "en_tendencia": false,
          "tallas": ["M", "L"]
        }
      },
      {
        "categoria": "Leggins",
        "producto": {
          "nombre": "Leggins deportivos negro",
          "cantidad": 14,
          "precio": 74900,
          "descuento": 15,
          "en_tendencia": true,
          "tallas": ["S", "M", "L"]
        }
      },
      {
        "categoria": "Pantalones",
        "producto": {
          "nombre": "Pantalón jeans rotos",
          "cantidad": 5,
          "precio": 139000,
          "descuento": 0,
          "en_tendencia": true,
          "tallas": ["S", "M", "L"]
        }
      },
      {
        "categoria": "Chaquetas",
        "producto": {
          "nombre": "Chaqueta de cuero negra",
          "cantidad": 6,
          "precio": 249900,
          "descuento": 10,
          "en_tendencia": true,
          "tallas": ["M", "L", "XL"]
        }
      },
      {
        "categoria": "Conjuntos",
        "producto": {
          "nombre": "Conjunto de pijama de algodón",
          "cantidad": 7,
          "precio": 89900,
          "descuento": 5,
          "en_tendencia": false,
          "tallas": ["S", "M"]
        }
      },
      {
        "categoria": "Jeans",
        "producto": {
          "nombre": "Jeans skinny negros",
          "cantidad": 10,
          "precio": 119000,
          "descuento": 0,
          "en_tendencia": true,
          "tallas": ["S", "M", "L"]
        }
      },
      {
        "categoria": "Pijamas",
        "producto": {
          "nombre": "Pijama de terciopelo negro",
          "cantidad": 4,
          "precio": 79900,
          "descuento": 0,
          "en_tendencia": false,
          "tallas": ["S", "M"]
        }
      }
    ],
    "agotado": [
      {
        "nombre": "Top corto blanco",
        "motivo_agotado": "Alta demanda en redes sociales",
        "reordenado": true,
        "fecha_estimada": "2025-05-12"
      },
      {
        "nombre": "Blazer oversize negro",
        "motivo_agotado": "Demora en importación",
        "reordenado": false,
        "comentario": "Se está evaluando cambio de proveedor"
      },
      {
        "nombre": "Vestido largo negro",
        "motivo_agotado": "No disponible por falta de producción",
        "reordenado": false,
        "comentario": "Producto descontinuado"
      },
      {
        "nombre": "Top de encaje",
        "motivo_agotado": "Alta demanda en redes sociales",
        "reordenado": true,
        "fecha_estimada": "2025-05-15"
      },
      {
        "nombre": "Botines de cuero",
        "motivo_agotado": "Retraso de proveedor",
        "reordenado": false,
        "comentario": "Evaluando alternativas"
      },
      {
        "nombre": "Pantalón de tiro alto",
        "motivo_agotado": "No disponible por retraso en producción",
        "reordenado": false,
        "comentario": "No se tiene fecha de reposición"
      },
      {
        "nombre": "Blusa con volantes",
        "motivo_agotado": "Alta demanda en tienda física",
        "reordenado": true,
        "fecha_estimada": "2025-05-20"
      },
      {
        "nombre": "Chaqueta de lana gris",
        "motivo_agotado": "Problemas de stock con proveedor",
        "reordenado": false,
        "comentario": "Buscando nuevo proveedor"
      },
      {
        "nombre": "Conjunto de verano",
        "motivo_agotado": "Retiro por defecto en fabricación",
        "reordenado": false,
        "comentario": "Sustitución en análisis"
      },
      {
        "nombre": "Falda de tul rosa",
        "motivo_agotado": "Alta demanda en tienda online",
        "reordenado": true,
        "fecha_estimada": "2025-05-18"
      }
    ],
    "en_camino": [
      {
        "nombre": "Falda plisada verde",
        "proveedor": "GreenStyle Colombia S.A.S.",
        "fecha_llegada_estimada": "2025-05-10",
        "motivo_retraso": "Retraso del proveedor internacional"
      },
      {
        "nombre": "Bota de invierno marrón",
        "proveedor": "Trendy Boots",
        "fecha_llegada_estimada": "2025-05-15",
        "motivo_retraso": "Demora por fabricación"
      },
      {
        "nombre": "Suéter gris melange",
        "proveedor": "Winter Wear Colombia",
        "fecha_llegada_estimada": "2025-05-20",
        "motivo_retraso": "Problemas de logística"
      },
      {
        "nombre": "Blusa estampada floral",
        "proveedor": "Floral Tees",
        "fecha_llegada_estimada": "2025-05-25",
        "motivo_retraso": "Demora en el envío"
      }
    ]
  },
  "ventas": {
    "productos_mas_vendidos": [
      {
        "nombre": "Vestido floral verano",
        "cantidad_vendida": 125
      },
      {
        "nombre": "Top corto blanco",
        "cantidad_vendida": 98
      },
      {
        "nombre": "Jeans mom fit azul claro",
        "cantidad_vendida": 76
      },
      {
        "nombre": "Chores de lino beige",
        "cantidad_vendida": 70
      }
    ]
  },
  "estadisticas": {
    "total_en_stock": 110,
    "total_agotado": 10,
    "total_en_camino": 4
  }
}
'''

# Cargar el JSON en Python
data = json.loads(json_data)

# Consultas
print("🧵 Productos en tendencia:")
for item in data['inventario']['en_tienda']:
    prod = item['producto']
    if prod['en_tendencia']:
        precio_con_descuento = prod['precio'] * (1 - prod['descuento'] / 100)
        print(f" - {prod['nombre']} ({precio_con_descuento} COP) - Tallas: {', '.join(prod['tallas'])} - Descuento: {prod['descuento']}%")

print("\n❌ Productos agotados:")
for prod in data['inventario']['agotado']:
    print(f" - {prod['nombre']} (Motivo: {prod['motivo_agotado']})")

print("\n🔥 Productos más vendidos:")
for prod in data['ventas']['productos_mas_vendidos']:
    print(f" - {prod['nombre']} ({prod['cantidad_vendida']} unidades)")

print("\n🚛 Productos en camino:")
for prod in data['inventario']['en_camino']:
    print(f" - {prod['nombre']} llegará el {prod['fecha_llegada_estimada']} (Motivo: {prod['motivo_retraso']})")

# Estadísticas
stats = data['estadisticas']
print(f"\n📊 Totales:")
print(f" - En stock: {stats['total_en_stock']}")
print(f" - Agotados: {stats['total_agotado']}")
print(f" - En camino: {stats['total_en_camino']}")


