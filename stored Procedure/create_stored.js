function greetCaller(name) {
    var context = getContext();
    var response = context.getResponse();
    response.setBody("Hello " + name);
}