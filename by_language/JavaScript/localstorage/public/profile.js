console.log('Loading...');

new Vue({
  el: '#app',
  data: {
    store: []
  },
  methods: {
    refresh: function() {
      let key;
      const storage = window.localStorage;
      this.store = [];
      for (let i = 0; i < storage.length; i += 1) {
        key = storage.key(i);
        this.store[i] = {key, value: storage.getItem(key)};
      }
    },
  }
});
