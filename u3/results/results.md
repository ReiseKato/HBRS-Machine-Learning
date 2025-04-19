# Prinzip Pearson Correlation Coefficient

Das Pearson Korrelations Koeffizient misst die lineare Ähnlichkeit zwichen zwei numerischen Vektoren. In diesem Datensatz ist es die Häufigkeit bestimmter Wörter in Blogposts. Man kann es sich also so vorstellen, dass ein Blog ein Vektor ist. Seine Elemente sind die Häufigkeiten bestimmer Wörter.

# Warum Pearson zum Klustern von Blog-Ähnlichkeiten über Wort-Häufigkeiten verwenden?

Blogs sind unterschiedlich lang. Heißt, dass in einem längeren Blog bestimmter Wörter häufiger auftauchen, als in kürzeren Blogs. Da der Pearson Koeffizient die absoluten Häufigkeiten ignoriert, ist es ein gutes Mittel zur Ermittlung der Ähnlichkeit zweier Blogs. Bsp.: Sei a = [1, 2, 3] und b = [10, 20, 30]. Pearson Koeffizient = 1.0 -> Perfekte Ähnlichkeit (gleich).
Da es beim Klustern um die Themen geht und nicht die Häufigkeiten ist, der Pearson Koeffizient somit ein gutes Mittel.

Ein weiterer Grund ist die hohe Skalierbarkeit. Aufgrund der Berechnungsart des Pearson Koeffizients (kann alle Dimensionen auf einmal einbeziehen) kann es auch Vektoren mit hunderten von Dimensionen umgehen. Wort-Häufigkeits-Vektoren sind in der Regel hoch dimensioniert.

Die semantische Ähnlichkeit wird durch die Ähnlichkeit der verwendeten Wörter gegeben. Blogs, die ein ähnliches Thema behandeln, werden ähnliche Wörter nutzen. Diese Ähnlichkeit wird von Natur aus höher gewichtet, als die rohe Häufigkeit von Wörtern.

Zusammenfassend lässt sich sagen: 
1. Vergleicht welche Wörter genutzt werden und NICHT wie häufig
2. Blogs verschiedener Längen sind vergleichbar
3. Klusterbildung nach semantischer Ähnlichkeit und NICHT Länge