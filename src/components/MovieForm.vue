<template>
    <!-- Form -->
    <form method="POST" enctype="multipart/form-data"  @submit.prevent="saveMovie" class = 'Mform' >
        <div class="form-group mb-3">
            <label for="title" class="Flabel">Movie Title</label>
            <input type="text" name="title" class="form-control">
        </div>
        <div class="form-group mb-3">
            <label for="description" class="form-label">Description:</label>
            <textarea name="description" class="form-control"></textarea>
        </div>
        
        <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster:</label>
        <input type="file"  name="poster" class="form-control">
      </div>

    </form>


    <script setup>
        fetch("/api/v1/movies", {method: 'POST'})
        .then(function (response){return response.json();})
        .then(function (data) {
                                // display a success message
                                console.log(data);
                                })
        .catch(function (error) {console.log(error);});


    </script>

</template>
