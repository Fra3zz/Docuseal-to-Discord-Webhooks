<H1>Info</H1>
<p>Takes the webhook request from <a href="https://github.com/docusealco/docuseal">docuseal</a> and passes it to a 
discord webhook. Filters the request info to the necissary info. Makes the request to discrod show as a comment from the
webhook bot.</p>


<H1>Environmental Variables</H1>
<ul>
    <p>Required</p>
    <li>WEBHOOK_URL = Make this your discord webhook url</li>
    <br>
    <p>Optional</p>
    <li>URL_PATH = Sets automatically to "/". Can be modified but must
        include a slash.
    </li>
</ul>

<H1>installation</H1>
<ol>
    Docker
    <li>Download the docker image and run image with set environment variables.</li>
</ol>
    File/Create your own docker image
<ol>
    <li>Download files from github repo.</li>
    <li>Install dependencies from requirements.txt filr via pip.</li>
    <li>Run with <div style="font-weight: bold;">flask run</div></li>
</ol>

