<template>
  <div>
    <div>
  <b-input-group id="control_width">
    <b-form-input type="text" v-model="content" @keyup.enter="commentCreate(content)"></b-form-input>
    <b-input-group-append>
      <b-button variant="info" style="color:white" @click="commentCreate(content)">입력</b-button>
    </b-input-group-append>
  </b-input-group>
</div>
  </div>
</template>

<script>
export default {
  name: 'Comments',
  data() {
    return {
      content: ""
    }
  },
  methods: {
    commentCreate: function (event) {
      this.$emit('createComment', event)
      this.content = ""
    }
  },

}
</script>

<style scoped>

#control_width {
  width: 70%;
  margin: 0 auto;
}

</style>