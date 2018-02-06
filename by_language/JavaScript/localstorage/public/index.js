console.log('Loading...');

new Vue({
  el: '#app',
  data: {
    key: '',
    value: ''
  },
  methods: {
    setPair: function() {
      console.log('Set.');
      window.localStorage.setItem(this.key, this.value);
    },
    redirect: function() {
      document.location.href = "profile.html";
    }
  }
});
