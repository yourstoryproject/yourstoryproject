import Route from '@ember/routing/route';

export default Route.extend({
  function() {
    this.transitionTo('not-found', 404);
  }
});
