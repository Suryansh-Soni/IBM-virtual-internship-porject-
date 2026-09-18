import streamlit as st
from PIL import Image

from waste_classifier import classify_image
from waste_rules import WASTE_RULES


st.set_page_config(
    page_title="WasteWise",
    page_icon="♻️",
    layout="centered"
)


st.title("♻️ WasteWise")

st.subheader(
    "AI-Powered Waste Classification & Segregation Assistant"
)

st.write(
    "Upload an image of a waste item and WasteWise will "
    "identify the object and provide responsible disposal guidance."
)

st.divider()


uploaded_file = st.file_uploader(
    "Upload your waste image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Analyze Waste"):

        with st.spinner("AI is analyzing the image..."):

            results = classify_image(image)

        st.subheader("AI Predictions")

        for result in results[:3]:

            label = result["label"]
            score = result["score"]

            st.write(
                f"**{label}** — {score:.2%}"
            )

        top_prediction = results[0]

        label = top_prediction["label"].lower()

        st.divider()

        matched_rule = None

        for keyword, rule in WASTE_RULES.items():

            if keyword in label:

                matched_rule = rule
                break


        if matched_rule:

            st.subheader("Waste Classification")

            st.write(
                f"**Category:** {matched_rule['category']}"
            )

            st.write(
                f"**Recommended Disposal:** "
                f"{matched_rule['bin']}"
            )

            st.info(
                f"💡 {matched_rule['tip']}"
            )

        else:

            st.warning(
                "The AI identified the object, but WasteWise "
                "does not have specific disposal guidance for it."
            )

            st.write(
                "Please check your local waste-management guidelines."
            )