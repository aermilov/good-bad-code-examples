import React, { useState, ChangeEvent, FC } from 'react';

// Define a type for the field
type Field = {
  type: 'text' | 'email' | 'password' | 'checkbox';
  name: string;
  label: string;
};

// Improved FormBuilder class with type safety
class FormBuilder {
  private fields: Field[];

  constructor() {
    this.fields = [];
  }

  addTextField(name: string, label: string): FormBuilder {
    this.fields.push({ type: 'text', name, label });
    return this;
  }

  addEmailField(name: string, label: string): FormBuilder {
    this.fields.push({ type: 'email', name, label });
    return this;
  }

  addPasswordField(name: string, label: string): FormBuilder {
    this.fields.push({ type: 'password', name, label });
    return this;
  }

  addCheckboxField(name: string, label: string): FormBuilder {
    this.fields.push({ type: 'checkbox', name, label });
    return this;
  }

  build(handleSubmit: (formData: Record<string, string | boolean>) => void): FC {
    const RenderForm: FC = () => {
      const [formData, setFormData] = useState<Record<string, string | boolean>>({});

      const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        const { name, value, type, checked } = e.target;
        setFormData(prevState => ({
          ...prevState,
          [name]: type === 'checkbox' ? checked : value,
        }));
      };

      const onSubmit = (e: React.SyntheticEvent) => {
        e.preventDefault();
        handleSubmit(formData);
      };

      return (
        <form onSubmit={onSubmit} style={{display: 'flex', flexDirection: 'column', minWidth: '300px', borderRadius: '16px', border: '1px solid #101010', padding: '8px'}}>
          {this.fields.map((field, index) => (
            <label key={index} style={{display: 'flex', justifyContent: 'space-between'}}>
              {field.label}
              <input
                type={field.type}
                name={field.name}
                checked={field.type === 'checkbox' ? !!formData[field.name] : undefined}
                value={field.type !== 'checkbox' ? (formData[field.name] as string) || '' : undefined}
                onChange={handleChange}
              />
            </label>
          ))}
          <button type="submit">Submit</button>
        </form>
      );
    };

    return RenderForm;
  }
}

export default FormBuilder;
