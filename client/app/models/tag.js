import DS from 'ember-data';

export default DS.Model.extend({
  created_on: DS.attr(),
  modified_on: DS.attr(),
  name: DS.attr(),
});
