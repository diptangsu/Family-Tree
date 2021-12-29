<template>
  <v-app id="inspire">
    <v-app-bar app>
      <v-toolbar-title>Family Tree</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text href="/logout">Logout</v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>

    <v-footer padless>
      <v-col class="text-center" cols="12">
        Done by a backend developer in a few hours so please don't judge the
        design. 🙂
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',
}
</script>
