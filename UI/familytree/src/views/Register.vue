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

    <v-text-field
      v-model="firstName"
      label="First Name"
      required
    ></v-text-field>

    <v-text-field v-model="lastName" label="Last Name" required></v-text-field>

    <v-text-field v-model="phone" label="Phone" required></v-text-field>

    <v-text-field v-model="address" label="Address" required></v-text-field>

    <v-text-field
      v-model="dob"
      label="Date of birth"
      type="date"
      required
    ></v-text-field>

    <v-btn :disabled="!valid" color="success" class="mr-4" @click="submit">
      Register
    </v-btn>
    <br />
    <br />

    <router-link to="/login">Login</router-link>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    email: '',
    password: '',
    firstName: '',
    lastName: '',
    phone: '',
    address: '',
    dob: '',
    emailRules: [
      (v) => !!v || 'E-mail is required',
      (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
  }),

  methods: {
    submit() {
      fetch(this.$store.state.baseUrl + '/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
          first_name: this.firstName,
          last_name: this.lastName,
          phone: this.phone,
          address: this.address,
          dob: this.dob,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === 'CREATED') {
            this.$router.push('/login')
          }
        })
        .catch((error) => console.error(error))
    },
  },
}
</script>
