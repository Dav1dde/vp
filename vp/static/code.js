




$(function() {
    window.cm = CodeMirror.fromTextArea(document.getElementById('code'), {
        mode: 'text',
        tabSize: 4,
        smartIndent: false,
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