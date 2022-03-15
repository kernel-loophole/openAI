import os
from string import ascii_lowercase
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline,smarter
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: hourse
Names: Ruff the check out, Wonder Canine, Sir Barks-a-Lot

Animal: {}
Names:""".format(
        animal.capitalize()
    )
