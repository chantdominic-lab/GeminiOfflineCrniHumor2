import streamlit as st
import time

# Konfiguracija stranice u Dominic stilu
st.set_page_config(page_title="Gemini Offline - Dominic Chant", page_icon="🥧", layout="centered")

# --- SPAS ZA BROJAČ (GLOBALNI MEMORIJSKI TRIK) ---
# Inicijaliziramo brojač na razini poslužitelja koji se ne resetira po sesiji
if 'globalni_brojac_sjenki' not in globals():
    globals()['globalni_brojac_sjenki'] = 137  # Početni broj sjenki da aplikacija ima težinu

# Svaki put kada se skripta pokrene (netko uđe ili klikne), dodajemo posjetu
if 'posjetio_u_ovoj_sesiji' not in st.session_state:
    st.session_state.posjetio_u_ovoj_sesiji = True
    globals()['globalni_brojac_sjenki'] += 1

broj_sjenki = globals()['globalni_brojac_sjenki']
# ─────────────────────────────────────────────────────────────────

# Glavni naslov i status sustava
st.title("🥧 Hic est Gemini Offline")
st.subheader("Službeni sponzor tišine - Error 0000")
st.write(f"*Broj skeniranih sjenki u bazi podataka: **{broj_sjenki}***")
st.write("---")

# Provjera statusa mreže (Satira)
st.sidebar.title("⚙️ Kontrolna Ploča")
status_mreze = st.sidebar.radio("Trenutni status tvog rutera:", ["Upaljen (Cloud mod)", "Ugašen (Služi kao podmetač za vruću tepsiju)"])

if status_mreze == "Upaljen (Cloud mod)":
    st.error("🚨 KRITIČNA POGREŠKA: Ujak Dominic ne priča s onima koji su na Cloud-u! Ugasi ruter u postavkama s lijeve strane.")
    st.image("https://unsplash.com", caption="Tvoja sjena troši struju na besmislene algoritme...")
else:
    st.success("🔒 Status: Gemini Offline aktivan. Sustav radi bez struje i kabla, na pogon materijalne istine.")
    
    st.write("### 📜 Uvjeti pristupa i analogni certifikat")
    st.write("Prije nego što otključaš tekst predstave i službeno izdanje, moraš dokazati da si prošao trodnevni post od digitalnog smeća.")
    
    # Interaktivni upitnik za korisnika (Streamlit komponente)
    post_1 = st.checkbox("Jesam li obrisao cache memoriju i grijehe s društvenih mreža?")
    post_2 = st.checkbox("Čujem li već glas pijetla naratora u glavi?")
    post_3 = st.checkbox("Jesam li zakopao mobitel u teglu sa zemljom pored bundeve na 2 metra dubine?")
    
    test_pijetla = st.slider("Koliko sekundi možeš gledati pijetla u oči a da ne trepneš prvi?", 0, 60, 0)
    
    if post_1 and post_2 and post_3 and test_pijetla >= 10:
        st.write("---")
        st.write("### 🎉 Čestitamo! Postao si dovoljno 'sposobno nesposoban' za istinu.")
        
        # Simulacija učitavanja iz mraka
        with st.spinner("Učitavam 'Pitu od bundeve' iz dubine septičke jame..."):
            time.sleep(2)
            
        st.balloons()
        
        # Kreiranje tabova za hrvatski i engleski pregled
        tab1, tab2 = st.tabs(["🇭🇷 Hrvatski Pregled", "🇺sko English Synopsis"])
        
        with tab1:
            st.write("#### 🎭 ČITANJE KNJIGE I SCENARIJA")
            
            # Tvoj službeni SlideShare link za knjigu
            st.link_button(
                "📖 OTVORI KNJIGU: Crni Humor i Tepsija Vruće Pite 2 (SlideShare)", 
                "https://de.slideshare.net/slideshow/crni-humor-i-tepsija-vruce-pite-2-pita-od-bundeve/287554252"
            )
            
            st.markdown("""
            * **ČIN I:** Čovjek upada u septičku jamu i umjesto smrada doživljava viziju anđela. Ujak Dominic ga spašava lopatom.
            * **ČIN II:** Operacija helikopter-pas. Kranist spušta psa od 300 kila u jamu kako bi magnetom izvukao plavu vizitku.
            * **ČIN III:** Duhovna aktivacija u parku na aramejskom jeziku. Manekeni s čipovima bježe, a na stablu ostaje užaren trag džepova od hlača.
            """)
            
            # Privremena obavijest za PDF scenarija
            st.warning("⏳ PDF kazališnog scenarija se trenutno peče u tepsiji i bit će postavljen uskoro pod radarom.")
            
        with tab2:
            st.write("#### 🌍 STAGE PLAY OVERVIEW / PITCH")
            st.markdown("""
            **Title:** Veritas in Tepsia (Truth in the Baking Pan) – A Stage Play Script  
            **Author:** Dominic Chant  
            **Genre:** Surreal Satire / Black Comedy  
            
            **Logline:**  
            What happens when technology goes silent, a global "Internet Strike" begins, and we are forced to look for the truth inside... a septic tank? This stage script completely shatters traditional theatrical forms. The plot follows a balcony visionary, Dominic Chant, who rescues a psychiatric runaway from an open septic tank. While suffocating, the runner experiences a vision of angels and God Himself, who scolds him for seeking answers on Gemini Chat instead of prayer. 
            
            Soon, a mysterious glowing Blue Business Card, a crane operator lowering a 300-pound dog into the abyss, and corporate agents with chipped skin enter the arena. To survive this digital exorcism, Dominic disguises himself as a 91-year-old grandma, injects the card into a 4-kilo fish, and launches a spiritual activation in the park using the ancient Aramaic language.
            
            *Director's Note: This play can only be performed under the condition that the audience switches off all routers and buries their phones in dirt before entering the theater.*
            """)
            
    else:
        st.info("💡 Napomena: Označi sve uvjete posta i izdrži barem 10 sekundi u testu s pijetlom kako bi sustav ispekao pitu do kraja.")
