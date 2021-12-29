<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <v-text-field
      v-model="password"
      label="Password"
      type="password"
      required
    ></v-text-field>

    <v-btn :disabled="!valid" color="success" class="mr-4" @click="submit">
      Login
    </v-btn>
    <br />
    <br />

    <router-link to="/register">Register</router-link>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    email: '',
    password: '',
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
  }),

  methods: {
    submit() {
      // this.$refs.form.validate()

      fetch(this.$store.state.baseUrl + '/authenticate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data)
          if (data.access_token) {
            this.$store.commit('setToken', data.access_token)
            this.$router.push('/person')
          } else {
            this.$router.push('/login')
          }
        })
    },
  },
}
</script>
