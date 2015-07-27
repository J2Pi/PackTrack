import Ember from 'ember';

export default Ember.Route.extend({
  model: function() {
    console.log('route called');
    //should later on return the list of packages currently being tracked
    //for now, it can just return nothing
  },

  setupController: function(controller, model) {
    controller.set('model', model);
  }
});
