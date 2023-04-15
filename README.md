# Python-Calculator

## First Steps

Google wie man in Python eine Weboberfläche kreieren kann -> Flask

## Flask Documentation

Zum installieren / Aufbau des Projektes in VSC und wie man Routings erstellt

## ChatGPT

Zum absichern für vernünftigen Code und für Verständnisfragen oder als Start für Recherchen.
Z.B.: "Ist es möglich die Creation von verschiedenen Buttons ins Python auszulagern anstatt im html viele Zeilen zu benötigen?"

## Mein Freund das Informatik Genie aka ChatGpt in besser

Zum absichern für vernünftigen Code und für Verständnisfragen oder als Start für Recherchen.
Z.B.: "Verwende nicht die Möglichkeit Buttons im Python zu erstellen. Dies ermöglicht XSS-Injections / Sicherheitslücken"

## Styling

Passierte schließlich alles an einem Tag und ist angelehnt an den IOS Taschenrechner.

## Problem: GET und POST

Die Entscheidung entweder Javascript zu verwenden um Eingaben ClientSite zu halten und dann ein HTTP request zu machen
oder nur Python verwenden, aber dann den Abstrich machen dass nur ein Client die Seite zu einer gegebenen Zeit verwenden kann,
da im Server die Eingabe in einer Variable gespeichert wird und damit golbal ist.

## Lösung:

Wir können lokal states im Browser halten, indem wir diese beim template rendern in ein hidden Input im HTML setzen
und es durch das POST Formular durch den Flask request im Python abfragen können.
