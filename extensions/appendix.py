"""Adopted from https://github.com/heig-tin-info/handout

Rename section number with alphabetic letters for ``.. appendix``
"""

import string
from docutils import nodes
from sphinx.environment.collectors.toctree import TocTreeCollector
from sphinx.directives.other import TocTree
from sphinx import addnodes
from typing import cast


def alphabize(n):
    """Convert a number to a alphabet number (such as Excel columns)."""
    out = ""
    while n > 0:
        n, remainder = divmod(n - 1, len(string.ascii_uppercase))
        out = string.ascii_uppercase[remainder] + out
    return out


def to_letter(secnum):
    if not secnum or len(secnum) == 0:
        return secnum

    secnum = list(secnum)
    return tuple([alphabize(secnum[0])] + secnum[1:])


class AppendixDirective(TocTree):
    def run(self):
        ret = super().run()
        ret[0][0]["appendix"] = True
        return ret


class Collector(TocTreeCollector):
    def parse_tree(self, env):
        def _walk_toc(node, titlenode, appendix=False):
            for subnode in node.children:
                if isinstance(subnode, (nodes.bullet_list, nodes.list_item, addnodes.only)):
                    _walk_toc(subnode, titlenode, appendix)
                elif isinstance(subnode, addnodes.compact_paragraph) and appendix:
                    reference = cast(nodes.reference, subnode[0])
                    reference["secnumber"] = to_letter(reference["secnumber"])
                elif isinstance(subnode, addnodes.toctree):
                    _walk_toctree(subnode)

        def _walk_toctree(toctreenode: addnodes.toctree, appendix=False) -> None:
            for _, ref in toctreenode["entries"]:
                if ref in env.tocs:
                    _walk_toc(env.tocs[ref], env.titles.get(ref), appendix)

                    if appendix:
                        env.toc_secnumbers[ref] = {
                            k: to_letter(v) for k, v in env.toc_secnumbers[ref].items()
                        }

        for docname in env.numbered_toctrees:
            doctree = env.get_doctree(docname)
            for toctreenode in doctree.traverse(addnodes.toctree):
                appendix = toctreenode.get("appendix", False)
                _walk_toctree(toctreenode, appendix)

    def assign_section_numbers(self, env):
        rewrite_needed = super().assign_section_numbers(env)
        self.parse_tree(env)
        return rewrite_needed


def setup(app):
    app.add_directive("appendix", AppendixDirective)
    app.add_env_collector(Collector)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
