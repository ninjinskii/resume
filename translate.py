from i18n.en import translations as en
from i18n.fr import translations as fr

import sys, re

i18n = { "fr": fr, "en": en }

def main():
    if len(sys.argv) < 2:
        print("Add argument 'fr' or 'en' to run the script")
        return

    lang = str(sys.argv[1])

    if lang != "en" and lang != "fr":
        print("Add argument 'fr' or 'en' to run the script")
        return

    with open("resume.html", "r") as input:
        lines = input.readlines()

        with open(f"resume-{lang}.html", "w") as output:
            for line in lines:
                output.write(inject(line, lang))


def inject(text, lang) -> str:
    i18nKey = re.search(r"(?<={{\s).+(?=\s}})", text)

    if i18nKey != None:
        translations = i18n[lang]
        translation = translations[i18nKey.group(0)]
        injected = re.sub(r"{{\s.+\s}}", translation, text)
        return injected
    else:
        return text


if __name__ == "__main__":
    main()
