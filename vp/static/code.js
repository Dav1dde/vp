




$(function() {
    window.cm = CodeMirror.fromTextArea(document.getElementById('code'), {
        mode: 'text/x-d',
        tabSize: 4,
        smartIndent: true,
        lineNumbers: true,
        lineWrapping: false,
        firstLineNumber: 1
    });

    function resize() {
        $('.CodeMirror').css('height', $(window).height()-120 + 'px');
    }

    $(window).resize(resize);
    resize();
});