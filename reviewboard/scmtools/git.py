import urlparse

# Python 2.5+ provides urllib2.quote, whereas Python 2.4 only
# provides urllib.quote.
try:
    from urllib2 import quote as urllib_quote
except ImportError:
    from urllib import quote as urllib_quote
from reviewboard.scmtools.errors import FileNotFoundError, \
                                        InvalidRevisionFormatError, \
                                        RepositoryNotFoundError, \
                                        SCMError
urlparse.uses_netloc.append('git')
        empty_change = self._is_empty_change(linenum)
        empty_change_linenum = linenum + GIT_DIFF_EMPTY_CHANGESET_SIZE

        # Only show interesting empty changes. Basically, deletions.
        # It's likely a binary file if we're at this point, and so we want
        # to process the rest of it.
        if empty_change and not file_info.deleted:
            return empty_change_linenum, None
                return linenum, file_info

            if self._is_binary_patch(linenum):
                return linenum + 1, file_info

            if self._is_diff_fromfile_line(linenum):
            file_info.data += self.lines[linenum] + "\n"
            linenum += 1
    def _is_empty_change(self, linenum):
        next_diff_start_linenum = linenum + GIT_DIFF_EMPTY_CHANGESET_SIZE

        if next_diff_start_linenum >= len(self.lines):
            return True

        next_diff_start = self.lines[next_diff_start_linenum]
        next_line = self.lines[linenum + 1]
        return ((next_line.startswith("new file mode") or
                 next_line.startswith("old mode") or
                 next_line.startswith("deleted file mode"))
                and next_diff_start.startswith("diff --git"))

        url_parts = urlparse.urlparse(self.path)
        url = url.replace("<filename>", urllib_quote(path))
        errmsg = p.stderr.read()
            if errmsg.startswith("fatal: Not a valid object name"):
        url_parts = urlparse.urlparse(path)