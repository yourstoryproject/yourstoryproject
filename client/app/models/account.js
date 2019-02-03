import DS from 'ember-data';

export default DS.Model.extend({
  created_on: DS.attr(),
  email: DS.attr(),
  last_login: DS.attr(),
});
