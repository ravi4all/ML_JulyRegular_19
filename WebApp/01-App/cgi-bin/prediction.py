import cgi
import SentimentAnalysis

form = cgi.FieldStorage()
rev = form.getvalue('review')

pred = SentimentAnalysis.test(rev)
if pred[0] == 0:
    y_pred = "Negative"
else:
    y_pred = "Positive"

print("Content-type text/html \r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Hello World</h1>")
print("Review is <b>{}</b>".format(rev))
print("Prediction is <b>{}</b>".format(y_pred))
print("</body>")
print("</html>")