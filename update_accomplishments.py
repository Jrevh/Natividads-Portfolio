from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')
text = text.replace(
    'Integer eu ante ornare amet commetus vestibulum blandit integer non. Adipiscing cubilia elementum integer. Integer eu ante ornare amet commetus.',
    'Selected academic and applied IT projects covering systems design, project management, and cybersecurity audit — with downloadable PDF reports available for each major deliverable.'
)
text = text.replace(
    '<a href="#" class="image"><img src="Projects/Figure 2 Gantt Chart of Happy Pixies Digital Event Management System.png" alt="Happy Pixies diagram placeholder" /></a>',
    '<a href="Projects/Happy Pixies Event Management System.pdf" class="image" target="_blank"><img src="Projects/Figure 2 Gantt Chart of Happy Pixies Digital Event Management System.png" alt="Happy Pixies diagram" /></a>'
)
text = re.sub(
    r'(\t\t\t\t\t\t\t<p><strong>Outcome:</strong> Delivered professional Audit Findings Report and Executive Summary detailing High to Very High risk rating, providing clear roadmap for NagaTech Solutions to achieve regulatory compliance\.</p>\s*)<p><strong>Course:</strong> IT Audit</p>',
    r"\1<p><a href=\"Projects/Nagatech IT AUDIT PROJECT.pdf\" target=\"_blank\">Download full IT audit PDF</a></p>\n\t\t\t\t\t\t\t<p><strong>Course:</strong> IT Audit</p>",
    text,
    flags=re.DOTALL
)
text = re.sub(
    r'<article>\s*<a href="#" class="image"><img src="images/pic01.jpg" alt="" /></a>\s*<div class="inner">\s*<h4>Possibly broke spacetime</h4>.*?<article>\s*<a href="#" class="image"><img src="images/pic02.jpg" alt="" /></a>.*?<article>\s*<a href="#" class="image"><img src="images/pic03.jpg" alt="" /></a>.*?</article>',
    '''<article class="accordion-item">
<a href="#" class="image"><img src="Projects/5.1 Process Flow Diagram.png" alt="Process flow diagram" /></a>
<div class="inner">
<h4 class="accordion-title">Process Flow Modeling & Improvement</h4>
<div class="accordion-details" style="display: none;">
<p><strong>Focus:</strong> Identified inefficiencies in legacy workflows and modeled improved business processes for operational clarity.</p>
<p><strong>Outcome:</strong> Structured process flow diagrams and documentation to support automation recommendations in academic IT projects.</p>
</div>
</div>
</article>
<article class="accordion-item">
<a href="#" class="image"><img src="Projects/5.6 Use Case Diagram.png" alt="Use case diagram" /></a>
<div class="inner">
<h4 class="accordion-title">User Interface & Requirements Prototyping</h4>
<div class="accordion-details" style="display: none;">
<p><strong>Focus:</strong> Developed interface prototypes and system requirement models using Figma and UML to support user-centered design.</p>
<p><strong>Outcome:</strong> Produced clear interaction flows and documentation that translated academic concepts into practical design solutions.</p>
</div>
</div>
</article>
<article class="accordion-item">
<a href="#" class="image"><img src="Projects/4.2 Process Flow Diagram of the current business processes.png" alt="Current business process flow diagram" /></a>
<div class="inner">
<h4 class="accordion-title">Team Collaboration & Systems Evaluation</h4>
<div class="accordion-details" style="display: none;">
<p><strong>Focus:</strong> Worked with teams to analyze, evaluate, and improve system design in academic IT initiatives.</p>
<p><strong>Outcome:</strong> Delivered scalable system recommendations and documented findings through diagrams, reports, and stakeholder analysis.</p>
</div>
</div>
</article>''',
    text,
    flags=re.DOTALL
)
path.write_text(text, encoding='utf-8')
