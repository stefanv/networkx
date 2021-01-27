import json
from pathlib import Path
import networkx as nx


class display_d3js:
    
    def __init__(self, G, js_path:str, html_path:str):
        """
        Parameters
        ----------
        
        G : graph
            A networkx graph
        js_path : str
            Path to JavaScript to include.  The content of `json`
            is provider as the `graph` variable in JavaScript.
        html_path: str
            Path to the HTML to render.  The JavaScript segment is
            automatically appended into the document body as a
            ``<script>`` tag.

        """
        self.js = Path(js_path).read_text()
        self.html = Path(html_path).read_text()
        if "<body>" not in self.html:
            raise RuntimeError("Require <body> tag inside HTML file")
        graph_json = json.dumps(nx.json_graph.node_link_data(G))
        graph_var = f"var graph = {graph_json};\n"
        script = graph_var + self.js
        self._html = self.html.replace(
            "</body>", f"\n<script>\n{script}\n</script>\n</body>"
        )

    def _repr_html_(self):
        return self._html
