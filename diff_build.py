diff --git a/build.py b/build.py
index b716a16..569874c 100644
--- a/build.py
+++ b/build.py
@@ -18,46 +18,53 @@ import oyaml as yaml
 import os
 
 import logging
-logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
+
+logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
 
 # custom jinja environments
 JINJA_ENVS = {
-    'default': jinja2.Environment(
-        trim_blocks = True,
-        lstrip_blocks = True,
-        loader = jinja2.FileSystemLoader(os.path.abspath('.')),
+    "default": jinja2.Environment(
+        trim_blocks=True,
+        lstrip_blocks=True,
+        loader=jinja2.FileSystemLoader(os.path.abspath(".")),
     ),
-    '.tex': jinja2.Environment(
-        block_start_string = r'\BLOCK{',
-        block_end_string = '}',
-        variable_start_string = r'\VAR{',
-        variable_end_string = '}',
-        comment_start_string = r'\#{',
-        comment_end_string = '}',
-        line_statement_prefix = '%%',
-        line_comment_prefix = '%#',
-        trim_blocks = True,
-        lstrip_blocks = True,
-        autoescape = False,
-        loader = jinja2.FileSystemLoader(os.path.abspath('.')),
+    ".tex": jinja2.Environment(
+        block_start_string=r"\BLOCK{",
+        block_end_string="}",
+        variable_start_string=r"\VAR{",
+        variable_end_string="}",
+        comment_start_string=r"\#{",
+        comment_end_string="}",
+        line_statement_prefix="%%",
+        line_comment_prefix="%#",
+        trim_blocks=True,
+        lstrip_blocks=True,
+        autoescape=False,
+        loader=jinja2.FileSystemLoader(os.path.abspath(".")),
     ),
 }
 
 parser = argparse.ArgumentParser(description=__doc__)
-parser.add_argument('--template', default='template/index_template.html', help='Template file')
-parser.add_argument('--publications', default='template/publications.yaml', help='Publications YAML file')
-parser.add_argument('--output', default='index.html', help='Output file')
-parser.add_argument('--debug', action='store_true', help='Debug mode (verbose logging)')
+parser.add_argument(
+    "--template", default="template/index_template.html", help="Template file"
+)
+parser.add_argument(
+    "--publications",
+    default="template/publications.yaml",
+    help="Publications YAML file",
+)
+parser.add_argument("--output", default="index.html", help="Output file")
+parser.add_argument("--debug", action="store_true", help="Debug mode (verbose logging)")
 
-if __name__ == '__main__':
+if __name__ == "__main__":
     args = parser.parse_args()
 
-    # enable debug messages if using debug flag 
+    # enable debug messages if using debug flag
     if args.debug:
         logging.getLogger().setLevel(logging.DEBUG)
 
-    # load publications yaml file 
-    with open(args.publications, 'r') as f:
+    # load publications yaml file
+    with open(args.publications, "r") as f:
         publications = yaml.safe_load(f)
 
     # debug: print publications by category
@@ -70,10 +77,12 @@ if __name__ == '__main__':
 
     # read template
     _, template_extension = os.path.splitext(args.template)
-    logging.debug(f'template_extension: {template_extension} ({"recognized" if template_extension in JINJA_ENVS else "unrecognized"})')
-    jinja_env = JINJA_ENVS.get(template_extension, JINJA_ENVS['default'])
+    logging.debug(
+        f'template_extension: {template_extension} ({"recognized" if template_extension in JINJA_ENVS else "unrecognized"})'
+    )
+    jinja_env = JINJA_ENVS.get(template_extension, JINJA_ENVS["default"])
     template = jinja_env.get_template(args.template)
 
     # write file
-    with open(args.output, 'w', encoding="utf-8") as f:
+    with open(args.output, "w", encoding="utf-8") as f:
         f.write(template.render(publications=publications))
