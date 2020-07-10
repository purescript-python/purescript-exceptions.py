import traceback


def showErrorImpl(err):
    try:
        # TODO: make sure implemeted as JS
        result = traceback.extract_stack(err)
        if result is None:
            return str(err)
        else:
            return result
    except Exception as e:
        # TODO: sometimes we don't get a viable `err`,
        # and that shouldn't penalize us
        # should we log this somehow?
        return str(err)

def error(msg):
    return Exception(msg)


def message(e):
    # TODO: fix implmentation
    return str(e)


# exports.message = function (e) {
#   return e.message;
# };


def name(e):
    return str(type(e))


# exports.name = function (e) {
#   return e.name || "Error";
# };


def stackImpl(just):
    def _nothing(nothing):
        def ap(e):
            result = traceback.extract_stack(e)
            if result is None:
                return nothing
            else:
                return just(result)

        return ap

    return _nothing


# exports.stackImpl = function (just) {
#   return function (nothing) {
#     return function (e) {
#       return e.stack ? just(e.stack) : nothing;
#     };
#   };
# };


def throwException(e):
    def ap():
        raise e

    return ap


# exports.throwException = function (e) {
#   return function () {
#     throw e;
#   };
# };


def catchException(c):
    def task(t):
        def ap():
            try:
                return t()
            # TODO: is this equvilant?
            except Exception as e:
                return c(e)()

        return ap

    return task


# exports.catchException = function (c) {
#   return function (t) {
#     return function () {
#       try {
#         return t();
#       } catch (e) {
#         if (e instanceof Error || Object.prototype.toString.call(e) === "[object Error]") {
#           return c(e)();
#         } else {
#           return c(new Error(e.toString()))();
#         }
#       }
#     };
#   };
# };
