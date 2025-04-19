# Aufgabe 3

Gegeben ist eine Wortliste für 100 Blogs (blogdata.txt/blogdata.json). Die erste Zeile beinhaltet die einzelnen Wörter. Jede weitere Zeile beginnt mit dem Blogtitel und es folgen, durch Tabs getrennt, die Häufigkeitswerte für die jeweiligen Wörter.

Nutzen Sie nach Möglichkeit python, um die Daten aus der Datei blogdata.json:

import pandas as pd

pd.read_json("blogdata.json"))

einzulesen und die folgenden Aufgaben zu lösen:

- Clustern Sie die Blogs mit Hilfe des Hierarchischen Clusterings. Nutzen Sie für die Bewertung der Ähnlichkeit von zwei Blogs den Pearson-Koefﬁzient.

- Warum kann dieser genutzt werden?

- Versuchen Sie Informationen aus den einzelnen Clustern zu ermitteln. Gibt es Blogs mit den gleichen Themengebieten/Interessen? Hierfür bietet python Ausgabemöglichkeiten für Bäume (siehe Segaran oder https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html oder, oder ...)

Alternativ:

- Nutzen Sie die Klasse Data.java, um die Wortliste einzulesen und aufzubereiten. (da die Abstandsfunktionen mit double arbeiten ist die Map, in der die Wortvorkommen gezählt werden, evtl anzupassen.)

- Clustern Sie die Blogs mit Hilfe des Hierarchischen Clusterings. Nutzen Sie für die Bewertung der Ähnlichkeit von zwei Blogs den Pearson-Koefﬁzient (siehe auch Metrics.java). - Warum kann dieser genutzt werden?

- Versuchen Sie Informationen aus den einzelnen Clustern zu ermitteln. Gibt es Blogs mit den gleichen Themengebieten/Interessen? Hierfür ist es hilfreich, eine einfache (Konsolen-basierte) Ausgabe des gesammten Clusters zu implementieren.