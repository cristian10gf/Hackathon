import yfinance as yf
from src.utils.constants import KEYS

sigla = yf.Ticker("GOOG").info
datos_financieros = {key:sigla[key] for key in KEYS}

empresa = {
    "nombre": "Desarrollos Tech S.A.",
    "mision": "Proveer soluciones innovadoras de software que potencien el éxito de nuestros clientes.",
    "vision": "Ser la empresa líder en desarrollo de software a nivel global, reconocida por nuestra calidad y compromiso.",
    "valores": ["Innovación", "Calidad", "Compromiso", "Trabajo en Equipo", "Integridad", "variedad"],
    "direccion": "Área metropolitana de, Kilómetro 5, Vía Puerto Colombia, Barranquilla, Atlántico",
    "telefono": "1234-5678",
    "correo": "contacto@desarrollostech.com",
    "historia": "Fundada en 2010, Desarrollos Tech S.A. comenzó como una pequeña startup enfocada en soluciones de software personalizadas. A lo largo de los años, la empresa ha crecido significativamente, ampliando su cartera de servicios y su base de clientes. Hoy en día, Desarrollos Tech S.A. es reconocida por su capacidad para ofrecer soluciones innovadoras y de alta calidad en diversas industrias. Con una década de experiencia, nos hemos establecido como un socio confiable para empresas que buscan transformar sus operaciones a través de la tecnología.",
    "servicios": [
        {"nombre": "Desarrollo de Aplicaciones Móviles", "descripcion": "Creamos aplicaciones móviles intuitivas y de alto rendimiento para iOS y Android, adaptadas a las necesidades específicas de nuestros clientes."},
        {"nombre": "Desarrollo de Software a Medida", "descripcion": "Desarrollamos soluciones de software personalizadas que se alinean perfectamente con los procesos y objetivos de negocio de nuestros clientes."},
        {"nombre": "Consultoría Tecnológica", "descripcion": "Ofrecemos asesoramiento experto para ayudar a nuestros clientes a elegir y implementar las mejores soluciones tecnológicas."},
        {"nombre": "Mantenimiento y Soporte", "descripcion": "Proporcionamos servicios continuos de mantenimiento y soporte para asegurar que los sistemas de nuestros clientes funcionen sin problemas."},
        {"nombre": "Integración de Sistemas", "descripcion": "Ayudamos a nuestros clientes a integrar diversos sistemas y aplicaciones para mejorar la eficiencia y la comunicación dentro de sus organizaciones."}
    ],
    "planes_futuros": [
        {"nombre": "Expansión Internacional", "descripcion": "Planeamos abrir nuevas oficinas en Europa y Asia en los próximos tres años."},
        {"nombre": "Desarrollo de Nuevos Productos", "descripcion": "Estamos trabajando en el lanzamiento de una nueva línea de productos basados en inteligencia artificial y machine learning."}
    ],
    "politicas_y_procedimientos": [
        {"nombre": "Política de Calidad", "descripcion": "Nos comprometemos a mantener los más altos estándares de calidad en todos nuestros proyectos."},
        {"nombre": "Política de Privacidad", "descripcion": "Protegemos la información personal y los datos de nuestros clientes con estrictas medidas de seguridad."}
    ],
    "certificaciones_y_premios": [
        {"nombre": "ISO 9001", "descripcion": "Certificación en Sistemas de Gestión de la Calidad."},
        {"nombre": "Premio Innovación Tecnológica 2022", "descripcion": "Reconocimiento por nuestras soluciones innovadoras en la industria del software."}
    ],
    "valores financieros": datos_financieros,
    "Estado Servidores Empresariales": "Funcionando, sin problemas, 100% de disponibilidad, 0% de errores, 1002 dias sin caidas, 3233 del ultimo mantenimiento, 0 mantenimientos programados",
    "cultura": "En Desarrollos Tech S.A., fomentamos un ambiente de trabajo colaborativo y de apoyo, donde se valora la creatividad y la innovación. Nos comprometemos a ofrecer oportunidades de desarrollo profesional a nuestros empleados y a mantener una cultura inclusiva y diversa. Creemos que un equipo diverso y motivado es clave para la innovación y el éxito sostenido.",
    "impacto_social": "La empresa participa activamente en iniciativas comunitarias y proyectos de responsabilidad social corporativa, incluyendo programas de formación tecnológica para jóvenes y apoyo a organizaciones sin fines de lucro. Estamos comprometidos con la sostenibilidad y trabajamos para reducir nuestro impacto ambiental a través de prácticas empresariales responsables.",
    "Horarios y asesoramientio": {
        "guia": "https://www.desarrollostech.com/guia_induccion",
        "calendario": "https://calendar.google.com/calendar/u/0/r?id=c_123456789@group.calendar.google.com"
    },
    "Estrategia Marketing": "Para impulsar el crecimiento y posicionamiento de Desarrollos Tech S.A. se propone una estrategia integral que combina marketing de contenidos, SEO, redes sociales, publicidad online, relaciones públicas y marketing de referencia. El enfoque se centra en crear contenido de valor para el público objetivo, compuesto principalmente por empresas que buscan soluciones de software personalizadas. Se buscará aumentar la visibilidad de la marca, generar leads cualificados y fidelizar a los clientes actuales.",
    "equipo": {
      "fundador": {
        "nombre": "Ana García",
        "puesto": "CEO",
        "descripcion": "Ana García es la fundadora y CEO de Desarrollos Tech S.A. Con más de 15 años de experiencia en la industria del software, Ana es una líder visionaria que ha guiado a la empresa hacia el éxito y el crecimiento continuo."
      },
    },
    "logros": {
      "proyectos_destacados": [
        {
          "nombre": "Plataforma de telemedicina",
          "descripcion": "Solución tecnológica para brindar atención médica a distancia en áreas rurales."
        },
        {
          "nombre": "Sistema de gestión de inventarios",
          "descripcion": "Aplicación web para optimizar la gestión de inventarios en empresas manufactureras."
        }
      ]
    },
    "relaciones": {
      "inversionistas": [
        {
          "organizacion": "Universidad de Stanford",
          "descripcion": "Colaboración en proyectos de investigación."
        },
        
      ]
    },
    "cronologia": [
      {
        "año": 2015,
        "evento": "Fundación de la empresa"
      },
        {
            "año": 2017,
            "evento": "Lanzamiento de la primera aplicación móvil"
        },
        {
            "año": 2019,
            "evento": "Expansión a nuevos mercados internacionales"
        },
        {
            "año": 2021,
            "evento": "Certificación ISO 9001"
        },
        {
            "año": 2022,
            "evento": "Premio a la Innovación Tecnológica"
        },
    ],
    "redes_sociales": {
      "facebook": "https://www.facebook.com/desarrollostech",
      "twitter": "https://twitter.com/desarrollostech",
      "linkedin": "https://www.linkedin.com/company/desarrollostech",
      "instagram": "https://www.instagram.com/desarrollostech"
    }
}