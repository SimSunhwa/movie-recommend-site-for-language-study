<template>
    <div>
        <component :is="currentStep" 
        @next="goToNextStep" 
        @previous="goToPreviousStep"
        @updateData="updateFormData"
        @submit="signUp"
        :form-data="formData"/>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useMovieStore } from '@/stores/movie';
import SignUpStep1 from '@/components/SignUpView/SignUpStep1.vue';
import SignUpStep2 from '@/components/SignUpView/SignUpStep2.vue';
import SignUpStep3 from '@/components/SignUpView/SignUpStep3.vue';
import SignUpStep4 from '@/components/SignUpView/SignUpStep4.vue';

const steps = [SignUpStep1, SignUpStep2, SignUpStep3, SignUpStep4]
const currentStepIndex = ref(0)
const store = useMovieStore()

// 단계별 입력 데이터 저장
const formData = ref({
    username:'',
    password1:'',
    password2:'',
    email:'',
    birth:'',
    last_name:'',
    first_name:'',
    nickname:'',
    study_level:''
})

// 현재 컴포넌트
const currentStep = computed(() => steps[currentStepIndex.value])

// 다음 단계 이동
const goToNextStep = function (){
    if (currentStepIndex.value < steps.length -1){
        currentStepIndex.value++
    }
}

// 이전 단계로 이동
const goToPreviousStep = function () {
    if (currentStepIndex.value > 0) {
        currentStepIndex.value--
    }
}

// 데이터 업데이트
const updateFormData = function (newData) {
    formData.value = {...formData.value, ...newData}
    console.log(formData.value)
    // store.signUp(formData)
}

const signUp = function (newData) {
    store.signUp(newData)
}
</script>

<style scoped>

</style>