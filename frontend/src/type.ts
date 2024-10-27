export interface FormProps {
  title: string;
  username: string;
  setUsername: React.Dispatch<React.SetStateAction<string | undefined>>;
  handler: () => Promise<void>;
  buttonText: string;
}
