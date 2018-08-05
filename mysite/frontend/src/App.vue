<template>
  <div id="app" :style='note'>
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {  
    return {
      note: {
        backgroundImage: "url(" + require("./assets/bg.jpg") + ") ",
        backgroundPosition: "right bottom",
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundAttachment: "fixed",
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding:0px;
  margin:0px;
  position:absolute;
  top:0px;
  left:0px;
  width:100%;
  height:100%;
  border:hidden;
}
</style>
