module vp;

private {
    import std.stdio;
    import std.net.curl : put;
    import std.uri : encodeComponent;
    import file = std.file;
    import std.array : join;

    version(Windows) {
        import core.sys.windows.windows;
    }
}

enum URL = "http://localhost:5000/";

void main(string[] args) {
    // no stdin stuff
    if(args.length == 1) {
        writefln("No arguments");
        return;
    }

    if(file.exists(args[1])) {
        put(URL, file.read(args[1]));
    } else {
        put(URL, args.join(" "));
    }
}