import streamlit as st
import qrcode             # <-- ESTA ES LA QUE FALTA
from io import BytesIO    # Para manejar la imagen en memoria
from PIL import Image     # Para procesar la imagen del QR
# --- CONFIGURACIÓN GLOBAL ---
mi_numero = "50585289131"

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Burguer's Queen", page_icon="👑", layout="wide")

# 2. ESTILOS Y ENCABEZADO (Unificado para evitar errores visuales)
st.markdown("""
    <style>
    .pink-gradient {
        background: linear-gradient(90deg, #FF69B4, #FFC0CB);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        margin-bottom: 25px;
    }
    div.stButton > button {
        background-color: #FFD1DC !important;
        color: #5D5D5D !important;
        border: 2px solid #FFC0CB !important;
        border-radius: 20px !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #FFB6C1 !important;
        border-color: #FF69B4 !important;
        color: black !important;
    }
    div.stButton > button:active, div.stButton > button:focus {
        background-color: #A2D9A1 !important;
        color: white !important;
        border-color: #76C776 !important;
    }
    .footer-real {
        background: linear-gradient(90deg, #FFC0CB, #FF69B4);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        margin-top: 50px;
    }
    .footer-real a { color: #D4AF37; text-decoration: none; font-weight: bold; }
    </style>
    
    <div class="pink-gradient">
        <h1>👑 Burguer's Queen 👑</h1>
        <p>¡Los mejores sabores hasta tus aposentos!</p>
    </div>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE DATOS
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

precios = {
    "Hamburguesa Clásica": 150.0, "Papas fritas": 80.0, "Bebidas": 45.0,
    "Suspiros de Princesa": 70.0, "Tarta de la Abadesa": 95.0, "Manjar del Jardín": 60.0
}

# 4. NAVEGACIÓN
st.sidebar.title("🍔 Menú Real")
opcion = st.sidebar.radio("Ir a:", ["Ver Menú", "Mi Pedido"])

if opcion == "Ver Menú":
    st.markdown("<h2 style='text-align: center;'>🏰 Banquete de la Corte</h2>", unsafe_allow_html=True)
    
    # --- SECCIÓN: PLATOS PRINCIPALES ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400")
        st.subheader("Hamburguesa de la Corte")
        st.write("Carne de res, queso, tomate, cebolla, pepinillos, lechuga y nuestra salsa especial.")
        st.write("**C$150.00**")
        if st.button("Añadir al pedido", key="hamb"):
            st.session_state.carrito.append("Hamburguesa Clásica")
            st.toast("¡Añadida!")

    with col2:
        st.image("https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400")
        st.subheader("Papas de su Alteza")
        st.write("Papas cortadas con la lanza de Juana de Arco, crujientes y con sal del mar Rojo.")
        st.write("**C$80.00**")
        if st.button("Añadir al pedido", key="papas"):
            st.session_state.carrito.append("Papas fritas")
            st.toast("¡Añadidas!")

    with col3:
        st.image("https://images.unsplash.com/photo-1543253687-c931c8e01820?w=400")
        st.subheader("Elixir de la Reina")
        st.write("Refrescante elixir burbujeante para acompañar tu banquete real.")
        st.write("**C$45.00**")
        if st.button("Añadir al pedido", key="beb"):
            st.session_state.carrito.append("Bebidas")
            st.toast("¡Copa llena!")

    st.markdown("<hr style='border: 1px dashed #FFC0CB;'>", unsafe_allow_html=True)
    
    # --- SECCIÓN: POSTRES ---
    st.markdown("<h3 style='text-align: center;'>🍰 Dulces del Reino</h3>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.image("https://images.unsplash.com/photo-1514517604298-cf80e0fb7f1e?w=400")
        st.subheader("Suspiros de Princesa")
        st.write("Delicados merengues horneados con esencia de vainilla real.")
        st.write("**C$70.00**")
        if st.button("Añadir al pedido", key="susp"):
            st.session_state.carrito.append("Suspiros de Princesa")
            st.toast("Dulzura añadida")

    with p2:
        st.image("https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=400")
        st.subheader("Tarta de la Abadesa")
        st.write("Tarta rústica rellena de crema pastelera y secretos del convento.")
        st.write("**C$95.00**")
        if st.button("Añadir al pedido", key="tart"):
            st.session_state.carrito.append("Tarta de la Abadesa")
            st.toast("Bendición dulce")

    with p3:
        st.image("https://images.unsplash.com/photo-1488477181946-6428a0291777?w=400")
        st.subheader("Manjar del Jardín")
        st.write("Frutos del bosque bañados en miel pura de las colinas de Rivas.")
        st.write("**C$60.00**")
        if st.button("Añadir al pedido", key="manj"):
            st.session_state.carrito.append("Manjar del Jardín")
            st.toast("Cosecha real")

elif opcion == "Mi Pedido":
    st.markdown("<h1 style='text-align: center;'>👑 Tu Alforja Real</h1>", unsafe_allow_html=True)
    if not st.session_state.carrito:
        st.warning("Tu alforja está vacía. ¡Visita el banquete!")
    else:
        subtotal = 0
        for item in st.session_state.carrito:
            p = precios.get(item, 0)
            st.write(f"🍴 {item} — **C${p:.2f}**")
            subtotal += p
        
        st.divider()
        iva = subtotal * 0.15
        total = subtotal + iva
        
        c1, c2 = st.columns([2, 1])
        with c2:
            st.write(f"Subtotal: C${subtotal:.2f}")
            st.write(f"IVA (15%): C${iva:.2f}")
            st.metric("Total Final", f"C${total:.2f}")
        
        # --- SUSTITUCIÓN DEL BOTÓN DE CONFIRMAR ---
        st.divider()
        
        # 1. Preparar el mensaje detallado (igual que en la barra lateral)
        resumen_pedido = ""
        total_pedido = 0
        conteo_items = {item: st.session_state.carrito.count(item) for item in set(st.session_state.carrito)}
        
        for item, cantidad in conteo_items.items():
            precio_unitario = precios.get(item, 0)
            subtotal_item = precio_unitario * cantidad
            resumen_pedido += f"- {cantidad}x {item} (C${subtotal_item:.2f})%0A"
            total_pedido += subtotal_item

        total_con_iva = total_pedido * 1.15
        mensaje_base = f"¡Hola! 👑 Me gustaría pedir:%0A{resumen_pedido}%0A*Total con IVA: C${total_con_iva:.2f}*%0A¿Me confirman el pedido?"
        
        # 2. El nuevo botón de acción final
        st.markdown(f"""
            <a href="https://wa.me/{mi_numero}?text={mensaje_base}" target="_blank" style="text-decoration: none;">
                <button style="
                    width: 100%;
                    background-color: #25D366;
                    color: white;
                    border: none;
                    padding: 15px;
                    border-radius: 10px;
                    font-weight: bold;
                    font-size: 18px;
                    cursor: pointer;
                    box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                    📲 Enviar Pedido por WhatsApp
                </button>
            </a>
            <br>
        """, unsafe_allow_html=True)
        
        # Botón opcional para limpiar la alforja después de pedir
        if st.button("Limpiar mi Alforja Real"):
            st.session_state.carrito = []
            st.rerun()

# --- GENERACIÓN DE QR (Agrégalo aquí) ---

# 1. Definir la función (puede ir al principio o aquí mismo)
def generar_qr(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#FF69B4", back_color="white")
    return img

# --- SECCIÓN DE PEDIDO DINÁMICO POR WHATSAPP ---
st.sidebar.markdown("---")
st.sidebar.write("### 🛒 Realiza tu pedido")

if st.session_state.carrito:
    # 1. Agrupar productos para que no se repitan (Ej: "2x Hamburguesa")
    resumen_pedido = ""
    total_pedido = 0
    
    # Contamos cuántas veces aparece cada item en el carrito
    conteo_items = {item: st.session_state.carrito.count(item) for item in set(st.session_state.carrito)}
    
    for item, cantidad in conteo_items.items():
        precio_unitario = precios.get(item, 0)
        subtotal_item = precio_unitario * cantidad
        resumen_pedido += f"- {cantidad}x {item} (C${subtotal_item:.2f})%0A"
        total_pedido += subtotal_item

    # 2. Configurar el mensaje final
    total_con_iva = total_pedido * 1.15
    mi_numero = "50585289131"
    mensaje_base = f"¡Hola! 👑 Me gustaría pedir:%0A{resumen_pedido}%0A*Total con IVA: C${total_con_iva:.2f}*%0A¿Me confirman el pedido?"
    
    # Botón dinámico
    st.sidebar.markdown(f"""
        <a href="https://wa.me/{mi_numero}?text={mensaje_base}" target="_blank" style="text-decoration: none;">
            <button style="width: 100%; background-color: #25D366; color: white; border: none; padding: 12px; border-radius: 10px; font-weight: bold; cursor: pointer;">
                🟢 Enviar Pedido a WhatsApp
            </button>
        </a>
    """, unsafe_allow_html=True)
else:
    st.sidebar.info("Agrega algo al menú para habilitar el pedido.")
# Configura tu número aquí (505 + tu número de Nicaragua)
mi_numero = "50585289131" # <--- ¡Pon tu número real aquí!
mensaje_wa = "¡Hola!Me gustaría realizar un pedido de Burguer's Queen. ¿Me podrían atender?"
mensaje_url = mensaje_wa.replace(" ", "%20")




# 2. Lógica para mostrarlo en la barra lateral
st.sidebar.markdown("---")
st.sidebar.write("### 📱 ¡Comparte el Menú!")

# REEMPLAZA ESTO con tu URL real cuando Streamlit te la dé
url_app = "https://burguers-queen-fkrsezj2ykgama4s3krkjg.streamlit.app/" 

if st.sidebar.button("Generar Código QR Real"):
    img_qr = generar_qr(url_app)
    
    # Preparar la imagen para Streamlit
    buf = BytesIO()
    img_qr.save(buf, format="PNG")
    st.sidebar.image(buf, caption="Escanea para compartir el banquete")

# 5. PIE DE PÁGINA 
st.markdown(
    """
    <div style="background-color: #FF69B4; padding: 20px; border-radius: 10px; text-align: center; color: white;">
        <p>📍 Ubicación: Calle Real del Castillo, Rivas</p>
        <p>⏰ Horario: 11:00 AM - 10:00 PM</p>
        <hr>
        <p style="font-size: 0.8em;">© 2026 Burguer's Queen - Sabores de Leyenda</p>
    </div>
    """,
    unsafe_allow_html=True
)