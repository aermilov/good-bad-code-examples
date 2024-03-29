import { useState } from 'react'
import FormBuilder from './FormBuilder';

function App() {
  const firstFormBuilder = new FormBuilder()
    .addTextField('firstName', 'First Name')
    .addEmailField('email', 'Email')
    .addPasswordField('password', 'Password')
    .addCheckboxField('agree', 'I agree to the terms and conditions');

  const FirstForm = firstFormBuilder.build((formData) => {
    console.log('Form data submitted:', formData);
  });

  const secondFormBuilder = new FormBuilder()
    .addCheckboxField('agre1', 'checkbox 1')
    .addCheckboxField('agre2', 'checkbox 2')
    .addCheckboxField('agre3', 'checkbox 3')

  const SecondForm = secondFormBuilder.build((formData) => {
    console.log('Form data submitted:', formData);
  });

  return (
    <div style={{ display: 'flex', justifyContent: 'center', gap: '32px' }}>
      <FirstForm />
      <SecondForm />
    </div>
  )
}

export default App
