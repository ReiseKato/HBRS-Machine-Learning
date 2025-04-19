# Warum bildet man ein Kluster über die Wörter?

Durch das Klustern der Wörter kann herausgefunden werden, welche Themenbereiche in den Blogs im vorliegenden Datensatz vertreten sind. Auch wie häufig bzw. wie stark. Auch kann der Trend der genutzten Wörter erkannt werden. Beispielsweise könen Dialekte heraus kristallisiert werden.

Man könnte es im Prinzip in etwa als den ersten Schritt Richtung NLP sehen. Durch das Gruppieren von Synonyen kann die Dimensionalität gesenkt werden -> Beschleunigung der Berechnung für spätere Zwecke. Dabei kann ein representatives Wort für diese Gruppe ausgewählt werden. Auch für Suchmaschinen interessant. So ist "code" sehr nah zu "script". Heißt eine Suchmaschine kann etwas mit script empfehlen, auch wenn explizit nach code gesucht wurde. -> Topic detection

Zusammenfassend ist es eine Art Karte der Vokabeln in diesem Datensatz. Eine Karte, die darauf aufbaut, wie Wörter verwendet werden, NICHT ihre lexikalische Bedeutung. "Script" könnte beispielsweise ähnlich verwendet werden wie "code"