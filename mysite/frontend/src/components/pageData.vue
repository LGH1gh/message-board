<template>
    <ul>
        <board MID = '1'></board>
    </ul>
</template>

<script>
import board from './board'
export default {
    components: {
        board
    },
    name: 'pageData',
    created() {
        console.log('pageData')
    }
}
</script>

<style scoped>

</style>
