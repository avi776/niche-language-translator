from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load the model and tokenizer
model_name = "facebook/nllb-200-distilled-600M"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, force_download=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, force_download=True)

# Create a translation pipeline
translator = pipeline('translation', model=model, tokenizer=tokenizer)

# Supported languages in FLORES-200 dataset with their language codes
lang_code_mapping = {  "English": "eng_Latn",
    "Romanian": "ron_Latn",
    "French": "fra_Latn",
    "German": "deu_Latn",
    "Spanish": "spa_Latn",
    "Italian": "ita_Latn",
    "Dutch": "nld_Latn",
    "Portuguese": "por_Latn",
    "Polish": "pol_Latn",
    "Russian": "rus_Cyrl",
    "Telugu": "tel_Telu",
    "Tajik (Cyrillic)": "tgk_Cyrl",
    "Tajik (Latin)": "tgk_Latn",
    "Thai": "tha_Thai",
    "Turkish (Latin)": "tur_Latn",
    "Ukrainian (Cyrillic)": "ukr_Cyrl",
    "Umbundu (Latin)": "umb_Latn",
    "Urdu (Arabic)": "urd_Arab",
    "Uzbek (Latin)": "uzb_Latn",
    "Vietnamese (Latin)": "vie_Latn",
    "Wolof (Latin)": "wol_Latn",
    "Xhosa (Latin)": "xho_Latn",
    "Yoruba (Latin)": "yor_Latn",
    "Zulu (Latin)": "zul_Latn",
    "Chinese (Simplified)": "zho_Hans",
    "Chinese (Traditional)": "zho_Hant",
    "Bengali": "ben_Beng",             # Bengali
    "Swahili": "swa_Latn",             # Swahili
    "Tagalog": "tgl_Latn",             # Tagalog
    "Punjabi": "pan_Guru",             # Punjabi (Gurmukhi script)
    "Malayalam": "mal_Mlym",           # Malayalam
    "Amharic": "amh_Ethi",             # Amharic
    "Kurdish (Kurmanji)": "kur_Latn",  # Kurdish (Kurmanji)
    "Haitian Creole": "hat_Latn",      # Haitian Creole
    "Pashto": "pus_Arab",              # Pashto (Arabic script)
    "Tigrinya": "tir_Ethi",            # Tigrinya (Ethiopic script)
    "Somali": "som_Latn",              # Somali
    "Maori": "mri_Latn",               # Maori
    "Hausa": "hau_Latn",               # Hausa
}

def translate_text(input_text, source_lang, target_lang):
    src_lang_code = lang_code_mapping.get(source_lang)
    tgt_lang_code = lang_code_mapping.get(target_lang)

    if not src_lang_code or not tgt_lang_code:
        return "Error: Invalid language selection."

    try:
        translated_text = translator(
            input_text,
            src_lang=src_lang_code,
            tgt_lang=tgt_lang_code
        )[0]['translation_text']
        return translated_text
    except Exception as e:
        return f"Error during translation: {str(e)}"