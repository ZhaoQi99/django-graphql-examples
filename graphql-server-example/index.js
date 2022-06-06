const { buildClientSchema } = require("graphql");
const fs = require("fs");
const { ApolloServer } = require("apollo-server");

const introspectionResult = JSON.parse(fs.readFileSync("../proj/schema.json"));
const schema = buildClientSchema(introspectionResult.data);

const server = new ApolloServer({
  schema,
  mocks: true,
});

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
