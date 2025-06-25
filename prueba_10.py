import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="CV de Leo Mattos", page_icon="💼", layout="wide")

# --- CARGAR FOTO DE PERFIL ---
foto = Image.open("foto_perfil.jpeg")

# --- ENCABEZADO ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image(foto, width=180)

with col2:
    st.title("Leonardo Richard Mattos Ramos")
    st.subheader("🎬 Comunicador Audiovisual | Director y Guionista | Desarrollador de Contenido")
    st.write("📍 Lima, Perú")
    st.write("📧 mattosleonardo73@gmail.com")
    st.write("📱 +51 926 904 605")

st.markdown("---")

# --- PERFIL PROFESIONAL ---
st.header("🧠 Perfil Profesional")
st.write("""
Apasionado por contar historias con imágenes, poseo una formación sólida en comunicación audiovisual, combinada con habilidades en dirección, edición, escritura de guiones y desarrollo de herramientas digitales para medios. 
Mi enfoque es crear contenidos memorables que conecten con el público, integrando creatividad, estrategia y tecnología.
""")

# --- EXPERIENCIA PROFESIONAL ---
st.header("💼 Experiencia Profesional")
st.write("**Director Cinematográfico – A34 Studios** *(2024 – Actualidad)*")
st.markdown("""
- Producción de programas y contenido digital para televisión.  
- Dirección de cortometrajes de ficción
- Supervisión de rodajes, edición y montaje de piezas para distintos formatos.  
- Gestión de equipos técnicos y creativos en proyectos de alto impacto.
""")

st.write("**Camarógrafo y Fotógrafo – A34 Studios** *(2024 – Actualidad)*")
st.markdown("""
- Logística de producción.
- Documentación de producciones audiovisuales   
- Operario de cámaras en rodajes de cortometrajes.  
- Participación en edición y revisión narrativa del montaje.
""")

# --- EDUCACIÓN ---
st.header("🎓 Educación")
st.write("**Pontificia Universidad Católica del Perú** – Estudiante de Comunicación Audiovisual *(2023 - Actualidad)*")

# --- CERTIFICACIONES ---
st.header("📜 Certificaciones")
st.markdown("""
- **Storytelling en el Cine y la Televisión** – PUCP, 2025  
- **Producción y edición profesional con Adobe Premiere** – Domestika, 2024  
- **Edición fotográfica** - Domestika, 2024
""")

# --- HABILIDADES TÉCNICAS ---
st.header("🛠️ Habilidades Técnicas")
st.markdown("""
- 🎬 Dirección de contenidos audiovisuales  
- 🖥️ Edición (Adobe Premiere, Lightroom Classic, DaVinci Resolve)  
- ✍️ Escritura de guiones y storytelling  
- 🧠 Python  
- 📱 Gestión de redes y contenido digital
""")

# --- HABILIDADES BLANDAS ---
st.header("🤝 Habilidades Blandas")
st.markdown("""
- 🧭 Liderazgo creativo  
- 🗣️ Comunicación efectiva  
- 🧘‍♂️ Manejo de estrés en producción  
- 👥 Trabajo en equipo interdisciplinario
""")

# --- PORTAFOLIO ---
st.header("📂 Portafolio Destacado")

st.subheader("🎞️ *Dulce Confesión* – Cortometraje de ficción")
st.markdown("[🔗 Ver en YouTube](https://www.youtube.com/watch?v=jexefE0B_SM)")

st.subheader("📺 *Spot Publicitario para A34 Studios*")
st.markdown("[🔗 Ver en YouTube](https://www.youtube.com/watch?v=3G5o78aExXI)")


# --- IDIOMAS ---
st.header("🌐 Idiomas")
st.markdown("""
- Español 🇵🇪 – Nativo  
- Inglés 🇬🇧 – Avanzado 
- Italiano 🇬🇧 – Básico
""")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown("**© 2025 Leo Mattos| Todos los derechos reservados**")
