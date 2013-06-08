




$(function() {
    window.cm = CodeMirror.fromTextArea(document.getElementById('code'), {
        mode: 'text/x-d',
        tabSize: 4,
        indentUnit: 4,
        indentWithTabs: true,
        smartIndent: true,
        lineNumbers: true,
        matchBrackets: true,
        lineWrapping: false,
        firstLineNumber: 1
    });

    function resize() {
        $('.CodeMirror').css('height', $(window).height()-120 + 'px');
        $('.CodeMirror-scroll').css('height', $(window).height()-120 + 'px');
    }

    $(window).resize(resize);
    resize();
});