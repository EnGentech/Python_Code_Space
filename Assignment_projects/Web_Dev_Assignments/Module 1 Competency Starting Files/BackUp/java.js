
var unirest = require("unirest");

var req = unirest("GET", "https://www.universal-tutorial.com/api/getaccesstoken");

req.headers({
    "Accept": "application/json",
    "api-token": "BlrIGzX05tDyPK2rInV1IV9ytRHoYPY4GI7YdJaWZKcKNTfUEQ4o-G5mcRB7NdLo3gc",
    "user-email": "engen.inyang@gmail.com"
});

req.end(function (res) {
    if (res.error) throw new Error(res.error);

    console.log(res.body);
});
